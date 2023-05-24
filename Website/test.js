function display(){
    let nob = parseInt(document.getElementById('nob').value);
    let models = document.getElementById('models').value;
    document.writeln(nob, " ", typeof nob);
    document.writeln('<br>', models, " ", typeof models);
}