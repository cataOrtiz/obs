/*$(document).ready(function(){
    $("#contenedorTwit").html("<div>prueba</div>");
})*/

$(document).ready(function(){
	$("#contenedorTwit").html("<div>prueba</div><div>prueba</div><div>prueba</div>");
})

$(document).ready(function(){
	$("#boton").click(function () {	
		alert($('input:radio[name=optionsRadios]:checked').val());
		$("#formulario").submit();
	});
});