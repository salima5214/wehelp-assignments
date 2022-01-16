
function showPicture(){
    let main = document.querySelector(".picture");

    for(let row = 1; row < 3; row++){
        for(let i = 4*(row-1); i < 4*row; i++){
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
        let mybr = document.createElement("div");
        mybr.className = "line_break";
        main.appendChild(mybr);
    }


}
// **********************************************

// **********************************************

let url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
let sight_information; // global variable

fetch(url).then((response) => {
    return response.json();
}).then( url_data => {  // local variable
    sight_information = url_data;
    showPicture();
});