console.log('JavaScript Beginner Projects: Tic Tac Toe!');

window.addEventListener('DOMContentLoaded', () => {
  _Setup();
});

const BOARD_STATE = {
  player: 'X',
  ai: 'O',
  blank: '',
  draw: 'draw',
};

let _GAMESTATE = null;

function _Setup() {
  _CreateBoard();
  _InitializeState();
}

function _CreateBoard() {
  const rows = document.getElementById('rows');
  for (let x = 0; x < 3; x++) {
    const curRow = document.createElement('div');
    curRow.id = 'row' + x;
    curRow.className = 'row';
    rows.appendChild(curRow);

    for (let y = 0; y < 3; y++) {
      const node = document.createElement('div');
      node.className = 'square';
      node.id = x + '.' + y;
      node.onclick = _HandlePlayerClick;
      curRow.appendChild(node);
    }
  }
}

function _InitializeState() {
  _GAMESTATE = {
    turn: BOARD_STATE.player,
    active: true,
  };
}

function _HandlePlayerClick(evt) {
  const isBlank = !evt.target.textContent.length;
  if (isBlank && _GAMESTATE.active && _GAMESTATE.turn == BOARD_STATE.player) {
    evt.target.textContent = BOARD_STATE.player;
    _GAMESTATE.turn = BOARD_STATE.ai;
    _CheckGameOver();
    if (_GAMESTATE.active) {
      setTimeout(_AISelectMove, 100);
    }
  }
}

function _CheckGameOver() {
  const winner = _EvaluateBoard(_GetBoardStates());
  if (winner === null) {
    return;
  }

  _GAMESTATE.active = false;

  let desc = '';

  if (winner === BOARD_STATE.ai) {
    desc = 'You lose!';
  } else if (winner === BOARD_STATE.player) {
    desc = 'You win!';
  } else {
    desc = 'Tie game, try again.'
  }

  document.getElementById('description').innerText = desc;
}

function _GetBoardStates() {
  const boardStates = [];
  for (let x = 0; x < 3; x++) {
    const row = [];
    for (let y = 0; y < 3; y++) {
      const node = document.getElementById(x + '.' + y);
      if (node.textContent === BOARD_STATE.player) {
        row.push(BOARD_STATE.player);
      } else if (node.textContent === BOARD_STATE.ai) {
        row.push(BOARD_STATE.ai);
      } else {
        row.push(BOARD_STATE.blank);
      }
    }
    boardStates.push(row);
  }
  return boardStates;
}

function _AISelectMove() {
  const boardStates = _GetBoardStates();
  const [_, choice] = _Minimax(boardStates, BOARD_STATE.ai);
  if (choice !== null) {
    const [x, y] = choice;
    document.getElementById(x + '.' + y).textContent = BOARD_STATE.ai;
    _GAMESTATE.turn = BOARD_STATE.player;
  }
  _CheckGameOver();
}

function _EvaluateBoard(boardStates) {
  const winningStates = [
    // Horizontals
    [[0, 0], [0, 1], [0, 2]],
    [[1, 0], [1, 1], [1, 2]],
    [[2, 0], [2, 1], [2, 2]],
    // Verticals
    [[0, 0], [1, 0], [2, 0]],
    [[0, 1], [1, 1], [2, 1]],
    [[0, 2], [1, 2], [2, 2]],
    // Diagonals
    [[0, 0], [1, 1], [2, 2]],
    [[2, 0], [1, 1], [0, 2]],
  ];

  for (const possibleState of winningStates) {
    let curPlayer = null;
    let isWinner = true;
    for (const [x, y] of possibleState) {
      const occupant = boardStates[x][y];
      if (curPlayer === null && occupant !== BOARD_STATE.blank) {
        curPlayer = occupant;
      } else if (curPlayer !== occupant) {
        isWinner = false;
        break;
      }
    }
    if (isWinner) {
      return curPlayer;
    }
  }

  if (boardStates.every(row => row.every(item => item !== BOARD_STATE.blank))) {
    return BOARD_STATE.draw;
  }

  return null;
}

function _Minimax(boardStates, player) {
  const winner = _EvaluateBoard(boardStates);
  if (winner === BOARD_STATE.ai) {
    return [1, null];
  } else if (winner === BOARD_STATE.player) {
    return [-1, null];
  } else if (winner === BOARD_STATE.draw) {
    return [0, null];
  }

  let bestScore = player === BOARD_STATE.ai ? -Infinity : Infinity;
  let move = null;

  for (let x = 0; x < 3; x++) {
    for (let y = 0; y < 3; y++) {
      if (boardStates[x][y] === BOARD_STATE.blank) {
        const newBoardStates = JSON.parse(JSON.stringify(boardStates));
        newBoardStates[x][y] = player;
        const [score] = _Minimax(newBoardStates, player === BOARD_STATE.ai ? BOARD_STATE.player : BOARD_STATE.ai);
        if (player === BOARD_STATE.ai) {
          if (score > bestScore) {
            bestScore = score;
            move = [x, y];
          }
        } else {
          if (score < bestScore) {
            bestScore = score;
            move = [x, y];
          }
        }
      }
    }
  }

  return [bestScore, move];
}
