// function RunPricePredictModel(area, pred_loc, pre_city, nob, models){
//     const { spawn } = require('child_process');

// // //const childPython = spawn('python', ['--version']);
// // // const childPython2 = spawn('python', ['backend.py', 'Area', 'No. of Bedrooms', 'City', 'Location', 'Resale']);
// //     const childPython = spawn('python', ['backend.py', area, nob, pre, pred_loc, '0', models]);
// // spawn('python', ['backend.py', '1675', '3', 'Banglore', 'Doddanekundi', '0', 'Random Forest']);

//     childPython.stdout.on('data', (data) => {
//         console.log(`stdout: ${data}`);
//         // document.writeln(data)
//         return data;
//     });

//     childPython.stderr.on('data', (data) => {
//         // console.error(`stderr: ${data}`);
//         return "Error"+data;
//     });

//     childPython.on('close', (code) => {
//         // console.log(`child process exited with code ${code}`);
//         return code;
//     }); 

// }

function getValues(){
    let user_name = document.getElementById("name").value;
    let user_mail = document.getElementById("mail").value;
    let user_location = document.getElementById("user_location").value;
    let user_phone_no = parseInt(document.getElementById("user_phone_no").value);
    let user_age = parseInt(document.getElementById("user_age").value);

    let area = parseInt(document.getElementById("area").value);
    let pred_loc = document.getElementById("pred_loc").value;
    let pre_city = document.getElementById("pre_city").value;
    let nob = parseInt(document.getElementById("area").value);
    let models = document.getElementById("models").value;

    // document.write(user_name, " ", typeof user_name);
    // document.write('<br>', user_mail, " ", typeof user_mail);
    // document.write('<br>', user_location, " ", typeof user_location);
    // document.write('<br>', user_phone_no, " ", typeof user_phone_no);
    // document.write('<br>', user_age, " ", typeof user_age);
    // document.write('<br>', area, " ", typeof area);
    // document.write('<br>', pred_loc, " ", typeof pred_loc);
    // document.write('<br>', pre_city, " ", typeof pre_city);
    // document.write('<br>', nob, " ", typeof nob);
    // document.write('<br>', models, " ", typeof models);

    const min = 5000000;
    const max = 40000000;

    let ans = Math.floor(Math.random() * ((max-min)+1) + min);
    document.getElementById("label-ans").innerHTML = "Rs : " + ans;
    event.preventDefault();
}