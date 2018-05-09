function printDays(string){

$(document).ready(function(){
    
    $('form').on('submit', function(event){

        $.ajax({
            type: "POST",
            url: "/days",
            data :{
                days: $('string').val()
            }
        })
    })

});

}

function printDays() {

    $(document).ready(function () {

        $('form').on('submit', function (event) {

            $.ajax({
                type: "POST",
                url: "/pee",
                data: {
                    days: $('string').val()
                }
            })
        })

    });
}