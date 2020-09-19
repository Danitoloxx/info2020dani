function insertarBBCode(tipo)
{
    switch(tipo)
    {
        case 'negrita':insertarTag(tipo, '[b]', '[/b]');break;
        case 'cursiva':insertarTag(tipo, '[i]', '[/i]');break;
        case 'subrayado':insertarTag(tipo, '[u]', '[/u]');break;
        case 'a-centro':insertarTag(tipo, '[center]', '[/center]');break;
        case 'imagen':imagen = prompt("Ingrese la URL de la imagen", "http://");
                      if(imagen != null){insertarTag(tipo , '[img]'+imagen, '[/img]');}break;
        case 'url':url = prompt("Ingrese la URL", "http://");
                   if(url != null){insertarTag(tipo, url, "");}break;
    }
}

function insertarTag(tipo, tag1, tag2)
{
    var nav = navigator.userAgent.toLowerCase();
    
    if(nav.indexOf("firefox") != -1 || nav.indexOf("chrome") != -1 || nav.indexOf("opera") != -1)
    {
        mensaje = document.getElementById('id_contenido');
        posicionInicial = mensaje.selectionStart;
        posicionFinal = mensaje.selectionEnd;
        inicio = mensaje.value.substr(0, posicionInicial);
        seleccionado = mensaje.value.substr(posicionInicial, (posicionFinal - posicionInicial));
        final = mensaje.value.substr(posicionFinal, (mensaje.value.length - posicionFinal));
        
        if(tipo == "imagen" || tipo == "video")
        {
            mensaje.value = inicio + tag1 + tag2 + seleccionado + final;
        }
        else if(tipo == "url")
        {
            if(posicionInicial == posicionFinal)
            {
                mensaje.value = inicio + '[url]' + tag1 + '[/url]' + final;
            }
            else
            {
                mensaje.value = inicio + '[url='+tag1+']' + seleccionado + '[/url]' + final;
            }
        }
        else
        {
            mensaje.value = inicio + tag1 + seleccionado + tag2 + final;
        }
    }
    else
    {
        alert("No hay soporte para este navegador");
       //ie11 nav.indexOf("rv:11.0") != -1)
       //ie nav.indexOf("msie") != -1
    }
}