// function toggleSidebar() {
//     const sidebar = document.getElementById('sidebar');
//     sidebar.classList.toggle('active');
// }

// base.js
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('active');
    const content = document.querySelector('.flex-grow-1');
    content.classList.toggle('active');
  }
  