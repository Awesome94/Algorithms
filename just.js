function numOffices(grid) {
    let result = 0;
    //Put your code here.
    let markLand = function (grid, x, y, visited) {
        if (x < 0 || x > grid.length - 1 || y < 0 || y > grid[x].length - 1) {
            return;
        }
        if (visited[x][y] === true) {
            return;
        }
        visited[x][y] = true;
        if (grid[x][y] === '0') {
            return;
        }
        markLand(grid, x - 1, y, visited);
        markLand(grid, x + 1, y, visited);
        markLand(grid, x, y - 1, visited);
        markLand(grid, x, y + 1, visited);
    };

    let visited = [];
    for (let i = 0; i < grid.length; i++) {
        visited[i] = [];
    }
    for (let x = 0; x < grid.length; x++) {
        for (let y = 0; y < grid[x].length; y++) {
            if (!visited[x][y] && grid[x][y] === '1') {
                result++;
                markLand(grid, x, y, visited);
            }
            visited[x][y] = true;
        }
    }
    return result;
};

let height = parseInt(readline());
let width = parseInt(readline());
let grid = [];
for (var i = 0; i < height; i++) {
    grid[i] = (readline() || "").split("");
}

print(numOffices(grid));