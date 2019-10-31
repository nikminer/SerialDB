function search(elem){
    var groups=document.getElementsByClassName("group")
    for (var indexgroup=1; indexgroup<groups.length;indexgroup++){
        var serials = groups[indexgroup].getElementsByClassName("serialname")
        for (var i=0; i<serials.length;i++){
            if (elem.value.length>0){
                parrent=findAncestor(serials[i],"serial")
                parrent.style.display ="none";
                if (serials[i].innerText.toUpperCase().includes(elem.value.toUpperCase()))
                    parrent.style.display ="flex";
            }
            else
                findAncestor(serials[i],"serial").style.display ="flex";  
        }
    }
}
function findAncestor (el, cls) {
    while ((el = el.parentElement) && !el.classList.contains(cls));
    return el;
}