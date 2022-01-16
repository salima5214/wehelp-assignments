
let row = 1;

function showPicture(){
    let main = document.querySelector(".picture");

    for(let i = 0; i < 2; i++){
        for(let j = 4*(row-1); j < 4*row; j++){
            
            if( j >= sight_information["result"]["results"].length ){
                let button = document.querySelector(".load_more>button");
                button.style.display = "none";
            }

            let box = document.createElement("div");
            box.className = "box";
            let img = document.createElement("img");
            img.src = "https://"+sight_information["result"]["results"][j]["file"].split("https://")[1];
            box.appendChild(img);      
            
            let img_name = document.createElement("div");
            img_name.className = "img_name";
            img_name.textContent = sight_information["result"]["results"][j]["stitle"];
            box.appendChild(img_name);
            main.appendChild(box);
        }
        let mybr = document.createElement("div");
        mybr.className = "line_break";
        main.appendChild(mybr);
        row += 1;
    }


}

// **********************************************


function loadMore() {
    showPicture();
}

// **********************************************
// len(data["result"]["results"])
// **********************************************

let url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
let sight_information; // global variable



fetch(url).then((response) => {
    return response.json();
}).then( url_data => {  // local variable
    sight_information = url_data;
    showPicture();
});

