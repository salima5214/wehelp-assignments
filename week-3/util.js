function showRow1(){
    let main = document.querySelector(".row_1");

    for(let i = 0; i < 4; i++){
        let box = document.createElement("div");
        box.className = "box";
        let img = document.createElement("img");
        img.src = "https://"+sight_information["result"]["results"][i]["file"].split("https://")[1];
        box.appendChild(img);      
        
        let img_name = document.createElement("div");
        img_name.className = "img_name";
        img_name.textContent = sight_information["result"]["results"][i]["stitle"];
        box.appendChild(img_name);
        main.appendChild(box);
    }

}

// **********************************************

function showRow2(){
    let main = document.querySelector(".row_2");

    for(let i = 4; i < 8; i++){
        let box = document.createElement("div");
        box.className = "box";
        let img = document.createElement("img");
        img.src = "https://"+sight_information["result"]["results"][i]["file"].split("https://")[1];
        box.appendChild(img);      
        
        let img_name = document.createElement("div");
        img_name.className = "img_name";
        img_name.textContent = sight_information["result"]["results"][i]["stitle"];
        box.appendChild(img_name);
        main.appendChild(box);
    }

}

// **********************************************

let url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
let sight_information; // global variable

fetch(url).then((response) => {
    return response.json();
}).then( url_data => {  // local variable
    sight_information = url_data;
    showRow1();
    showRow2();
});