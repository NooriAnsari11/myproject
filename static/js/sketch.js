const boardSizeInput = document.getElementById("#board_size");
const solveButton = document.getElementById('solve_button');
const boardDiv = document.getElementById('board');

let N = 8; // Default board size

solveButton.addEventListener('click', () => {
  N = parseInt(boardSizeInput.value, 10);
  solveNQueens(N);
});

function solveNQueens(N) {
  const board = Array.from({ length: N }, () => Array(N).fill('.'));
  const solutions = [];

  function isSafe(row, col) {
    // Check if a queen can be placed at this position
    for (let i = 0; i < row; i++) {
      if (board[i][col] === 'Q') return false;
      const diff = row - i;
      if (col - diff >= 0 && board[i][col - diff] === 'Q') return false;
      if (col + diff < N && board[i][col + diff] === 'Q') return false;
    }
    return true;
  }

  function backtrack(row) {
    if (row === N) {
      solutions.push([...board.map(row => row.join(''))]);
      return;
    }

    for (let col = 0; col < N; col++) {
      if (isSafe(row, col)) {
        board[row][col] = 'Q';
        backtrack(row + 1);
        board[row][col] = '.';
      }
    }
  }

  backtrack(0);

  displaySolutions(solutions);
}

function displaySolutions(solutions) {
  boardDiv.innerHTML = '';

  if (solutions.length === 0) {
    boardDiv.innerHTML = '<p>No solution found.</p>';
    return;
  }

  solutions.forEach((solution, index) => {
    const boardContainer = document.createElement('div');
    boardContainer.className = 'board-container';

    solution.forEach(row => {
      const rowDiv = document.createElement('div');
      rowDiv.className = 'row';

      row.split('').forEach(cell => {
        const cellDiv = document.createElement('div');
        cellDiv.className = 'cell';
        cellDiv.textContent = cell;
        rowDiv.appendChild(cellDiv);
      });

      boardContainer.appendChild(rowDiv);
    });

    boardContainer.style.border = '2px solid #333';
    boardContainer.style.margin = '10px';
    boardContainer.style.display = 'inline-block';
    boardDiv.appendChild(boardContainer);
  });
}

solveNQueens(N);
