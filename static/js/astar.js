const gridSize = 20;
let grid = new Array(gridSize);

// create 2D array
for (let i = 0; i < gridSize; i++) {
    grid[i] = new Array(gridSize);
}

// create HTML elements for each cell
let gridElement = document.getElementById('grid');
for (let y = 0; y < gridSize; y++) {
    for (let x = 0; x < gridSize; x++) {
        let cellElement = document.createElement('div');
        cellElement.classList.add('cell');
        cellElement.dataset.x = x;
        cellElement.dataset.y = y;
        cellElement.onclick = toggleWall;
        gridElement.appendChild(cellElement);
        grid[x][y] = {
            x: x,
            y: y,
            f: 0,
            g: 0,
            h: 0,
            element: cellElement,
            neighbor: getNeighbors(x, y)
        };
    }
    let breakElement = document.createElement('br');
    gridElement.appendChild(breakElement);
}

function toggleWall(e) {
    let x = e.target.dataset.x;
    let y = e.target.dataset.y;
    if (e.target.classList.contains('wall')) {
        e.target.classList.remove('wall');
        grid[x][y].wall = false;
    } else {
        e.target.classList.add('wall');
        grid[x][y].wall = true;
    }
}

function getNeighbors(x, y) {
    let neighbors = [];
    if (x > 0) neighbors.push(grid[x - 1][y]);
    if (y > 0) neighbors.push(grid[x][y - 1]);
    if (x < gridSize - 1) neighbors.push(grid[x + 1][y]);
    if (y < gridSize - 1) neighbors.push(grid[x][y + 1]);
    return neighbors;
}

function heuristic(a, b) {
    // Manhattan distance
    return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
}

function startPathfinding() {
    let start = grid[0][0];
    let end = grid[gridSize - 1][gridSize - 1];
    start.element.classList.add('start');
    end.element.classList.add('end');
    let openSet = [start];
    let closedSet = [];

    while (openSet.length > 0) {
        // find node in openSet with lowest f
        let lowestIndex = 0;
        for (let i = 0; i < openSet.length; i++) {
            if (openSet[i].f < openSet[lowestIndex].f) {
                lowestIndex = i;
            }
        }
        let current = openSet[lowestIndex];

        // end condition
        if (current === end) {
            console.log('Path found!');
            return;
        }

        // move current node to closedSet
        openSet.splice(lowestIndex, 1);
        closedSet.push(current);

        // check neighbors
        let neighbors = current.neighbors;
        for (let i = 0; i < neighbors.length; i++) {
            let neighbor = neighbors[i];

            if (!closedSet.includes(neighbor) && !neighbor.wall) {
                let tempG = current.g + 1;

                if (openSet.includes(neighbor)) {
                    if (tempG < neighbor.g) {
                        neighbor.g = tempG;
                    }
                } else {
                    neighbor.g = tempG;
                    openSet.push(neighbor);
                }

                neighbor.h = heuristic(neighbor, end);
                neighbor.f = neighbor.g + neighbor.h;
                neighbor.previous = current;
            }
        }
    }
    if (current === end) {
        console.log('Path found!');
        reconstructPath(current);
        return;
    }
    
    // no solution
    console.log('No solution!');
}
function reconstructPath(node) {
    while (node) {
        node.element.classList.add('path');
        node = node.previous;
    }
}
