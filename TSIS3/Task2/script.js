const  inputBox = document.getElementById("input-box")
const  listContainer = document.getElementById("list-container")
function addTask(){
    if(inputBox.value === ''){
        Swal.fire("Enter some text first !");    }
    else{
        let li = document.createElement("li");
        li.innerHTML=inputBox.value;
        listContainer.appendChild(li);
        let span = document.createElement("span")
        span.innerHTML = "\u00d7"
        li.appendChild(span);
        // let cnt = 0;
        // for(let i = 0; i < inputBox.value.length; i++){
        //     if(inputBox.value[i] >='0' && inputBox.value[i] <='9'){
        //         cnt++;
        //     }
        // }
        // console.log(cnt);
    }
    inputBox.value = "";
    saveData();
}

document.getElementById('input-box').addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        addTask();
    }
});

listContainer.addEventListener("click", function (e){
    if(e.target.tagName === "LI"){
        e.target.classList.toggle("checked");
        saveData();
    }
    else if(e.target.tagName === "SPAN"){
        e.target.parentElement.remove();
        saveData();
    }
}, false);

function saveData(){
    localStorage.setItem("data", listContainer.innerHTML);
}
function showTask(){
    listContainer.innerHTML = localStorage.getItem("data");
}
showTask();
