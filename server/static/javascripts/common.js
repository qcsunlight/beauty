$('#submit').click(function() {
    $.ajax({
        type: "POST",
        url: "/beauty/upload/",
        cache: false,
        data: new FormData($("#send-form")[0]),
        processData: false,
        contentType: false,
        success: function(data) {
            console.log(data);
            var obj = data;
            var age = obj['age'];
            var beauty = obj['beauty'];
            document.getElementById('age').innerHTML = "年龄： " + age;
            document.getElementById('beauty').innerHTML = "颜值： " + beauty;
        },
        error: function() {
            window.reload();
        }
    });
});

$('#upfile').change(function() {
		document.getElementById('age').innerHTML = '';
    document.getElementById('beauty').innerHTML = '';
    var file = $('#upfile').get(0).files[0];
    var reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = function(e) {
        $('#image').get(0).src = e.target.result;
    }
});