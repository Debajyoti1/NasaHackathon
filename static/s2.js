var getData = $.get('/df2');
getData.done(function(df2){
console.log(df2.district[0]);
for(var i=0;i<692;i++){
    document.getElementById("dd").innerHTML += '<a class="dropdown-item" href="#">'+df2.district[i]+'</a>';
}
});