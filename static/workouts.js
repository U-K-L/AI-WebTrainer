days = [false,false,false,false,false,false,false]
dayCount = 0
function SelectedDays(string) {
    if (string == "sunday") {
        alert("SUNDAY");
    }
    else if (string == "monday"){
        alert('MONDAY');
        document.getElementById('monday').style.backgroundColor = 'red';
        
        //document.querySelector('#monday').innerHTML = "WHAT";
    }
}

function daysSelected()
{
    for(i = 0; i < 7; i++){
        if(days[i] == true){
            dayCount++;
        }
    }
    if(dayCount > 2)
    {
        deniedChange = true;
    }
}

