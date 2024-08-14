// scrip para o modal de doação
const dialog = document.querySelector("#modalDialog");
const openButtom = document.querySelector("#openButtom");
const closeButtom = document.querySelector("#closeButton");

openButtom.addEventListener("click", (e) => {
    dialog.showModal();
});

closeButton.addEventListener("click", (e) => {
    dialog.close();
});