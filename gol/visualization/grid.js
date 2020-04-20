
let w;
let columns;
let rows;
let board;
let next;

function setup() {
  createCanvas(1000, 1000);
  w = 10;
  // Calculate columns and rows
  columns = floor(width / w);
  rows = floor(height / w);
  // Wacky way to make a 2D array is JS
  board = new Array(columns);
  for (let i = 0; i < columns; i++) {
    board[i] = new Array(rows);
  }
  // Going to use multiple 2D arrays and swap them
  next = new Array(columns);
  for (i = 0; i < columns; i++) {
    next[i] = new Array(rows);
  }
  //init();
}

function draw() {
  background(255);
  generate();
  for ( let i = 0; i < columns;i++) {
    for ( let j = 0; j < rows;j++) {
      if ((board[i][j] == 1)) fill(0);
      else fill(255);
      stroke(0);
      rect(i * w, j * w, w-1, w-1);
    }
  }

}

// reset board when mouse is pressed
function mousePressed() {
  //init();
}

// Fill board randomly
function init() {
  for (let i = 0; i < columns; i++) {
    for (let j = 0; j < rows; j++) {
      // Lining the edges with 0s
      if (i == 0 || j == 0 || i == columns-1 || j == rows-1) board[i][j] = 0;
      // Filling the rest randomly
      else board[i][j] = floor(random(2));
      next[i][j] = 0;
    }
  }
}

function generate() {
  fetch('http://gol.kta.io:5000/data/test.json')
    .then(response => {
      return response.json()
    })
    .then(data => {
      for (let x = 0; x < data.length; x++) {
        for (let y = 0; y < data.length; y++) {
           next[x][y] = data[x][y];
        }
      }
    })
    .catch(err => {
      console.log(err);
    })

  // Swap!
  let temp = board;
  board = next;
  next = temp;
}
