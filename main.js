const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

// 載入左右眼圖片
const leftImg = new Image();
const rightImg = new Image();
leftImg.src = "assets/left_view.jpg";
rightImg.src = "assets/right_view.jpg";

console.log("Dlon 🚀");

// 當圖片載入後初始化繪製
Promise.all([
  new Promise(resolve => leftImg.onload = resolve),
  new Promise(resolve => rightImg.onload = resolve)
]).then(() => {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

  let offset = 0;

  document.addEventListener("mousemove", (e) => {
    offset = (e.clientX / window.innerWidth - 0.5) * 20; // 模擬視差
    draw();
  });

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.globalAlpha = 1;
    ctx.drawImage(leftImg, -offset, 0, canvas.width, canvas.height);
    ctx.globalAlpha = 0.5;
    ctx.drawImage(rightImg, offset, 0, canvas.width, canvas.height);
  }

  draw();
});
