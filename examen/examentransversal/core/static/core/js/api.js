$(document).ready(function () {

    d = document.getElementById("respuesta");

    $("#buscar").click(function () {

        d.innerHTML = "" // Limpiar el contenedor
        var busqueda = $("#busqueda").val();

        //API de REST Countries
        const settings = {
            "async": true,
            "crossDomain": true,
            "url": "https://restcountries.eu/rest/v2/name/" + busqueda,
            "method": "GET"
        };

        $.ajax(settings).done(function (response) {
            console.log(response); // Respuesta en la consola para ver los elementos de la respuesta
            d.innerHTML += "El nombre es: " + response[0].name + "<br>La capital es: " + response[0].capital + "<br>Tiene una poblacion de aproximadamente: " + response[0].population + " personas" + "<br>El idioma es: " + response[0].languages[0].nativeName + "<br>La bandera es: <img id='bandera' src='" + response[0].flag + "' alt='Bandera'>"
        });

    });

});