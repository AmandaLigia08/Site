document.addEventListener("DOMContentLoaded", function () {
    emailjs.init("saTt1aqyAlTstrYk1"); // Substitua pelo seu User ID do EmailJS

    document.querySelector(".rd-mailform").addEventListener("submit", function (event) {
        event.preventDefault();

        let submitButton = document.querySelector(".button-primary");
        submitButton.disabled = true;
        submitButton.innerText = "Enviando...";

        // Capturar os valores do formulário
        let formData = {
            name: document.getElementById("contact-name").value,
            email: document.getElementById("contact-email").value,
            phone: document.getElementById("contact-phone").value,
            message: document.getElementById("contact-message").value,
        };

        // Enviar os dados via EmailJS
        emailjs.send("service_y9iayev", "template_3glndmj", formData)
            .then(function (response) {
                alert("Mensagem enviada com sucesso!");
                document.querySelector(".rd-mailform").reset();

                // Reativar o botão após o envio
                submitButton.disabled = false;
                submitButton.innerText = "Enviar";
            })
            .catch(function (error) {
                alert("Erro ao enviar a mensagem. Tente novamente mais tarde.");
                console.error("Erro:", error);

                // Reativar o botão após erro
                submitButton.disabled = false;
                submitButton.innerText = "Enviar";
            });
    });
});
