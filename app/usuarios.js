function Usuario () {
  this.email = 0;
  this.password = 0;
};

function insertUsuario () {
  try {
    var val_email = $('#email').val();
    var val_password = $('#name').val();
    var myUsuario = new Usuario();
    myUsuario.email = val_email;
    myUsuario.password = val_password;
    this.urlImage = sessionStorage.urlImage;

    var form_data = new FormData();
    form_data.append("email", myUsuario.email);
    form_data.append("password", myUsuario.password);

    jQuery.support.cors = true;
    jQuery.ajax({
      url: "/createUser",
      dataType: "text",
      cache: false,
      contentType: false,
      processData: false,
      data: form_data,
      type: "post",
      crossDomain: true,
      success: function () {
        alert ("Mensaje Enviado");
        $('#email').val(String.empty);
        $('#name').val(String.empty);
        $('#message').val(String.empty);
      },
      error: function(error) {
        alert(error)
      }
    });
  } catch (error) {
    alert(error)
  }
}

function getAllUsers () {
  jQuery.support.cors = true;
  try {
    $.ajax({
      url: "/readAllUser",
      dataType: 'json',
      cache: false,
      contentType: false,
      processData: false,
      type: 'get',
      crossDomain: true,
      success: function (response) {
        $("#IstUsers").empty();
        tweets = response;
        alert(response);

        var myTableUsers = "<table class='table table-striped table-advance table-hover'>" +
          " <tbody id='devices'> " +
          " <tr> " +
          " <th> </th> " +
          " <th> entitykey </th> " +
          " <th> email </th> " +
          " <th> password </th> " +
          " <th> Delete </th> " +
          " </tr> ";
        tweets.forEach(function (tweet) {
          myTableUsers += "<tr>" +
            "<td>" +
            "<button onclick='getOneUser(\"" + tweet.id +
            "\")' class='btn btn-primary'> " +
            " <i class='fa fa fa-ban'></i> (R)eadOne</button>" +
            "</td>" +
            "<td>" + tweet.id + "</td>" +
            "<td>" + tweet.email + "</td>" +
            "<td>" + tweet.passwd + "</td>" +
            "<td>" +
            "<button onclick='deleteUser(\"" + tweet.id + "\")' class='btn btn-danger'>" +
            "<i class= 'fa fa fa-ban'></i> (D)elete </button>" +
            "</td>" +
            "</div>" +
            "</td>" +
            "</tr>";
        });
        myTableUsers += "</tbody>" +
          "</table>";
        $("#IstUsers").append(myTableUsers);
      }
    });
  } catch (e) {
    alert("error: " + e);
  }
}


function deleteUser (userKey) {
  try {
    alert(userKey);
    var form_data = new FormData();
    form_data.append("key", userKey);
    jQuery.support.cors = true;
    jQuery.ajax({
      url: "/deleteUser",
      dataType: "text",
      cache: false,
      contentType: false,
      processData: false,
      data: form_data,
      type: "post",
      crossDomain: true,
      success: function (response) {
        alert("key eliminada: " + response);
      },
      error: function (error) {
        alert(error)
      }
    });
  } catch (error) {
    alert(error)
  }
}

function uploadDemo()
{

    var file_data = $("#uploaded_file").prop("files")[0];
    var form_data = new FormData();
    form_data.append("uploaded_file", file_data)

    jQuery.support.cors = true;
    try
    {
     $.ajax({
                url: "http://localhost:8080",
                dataType: 'text',
                cache: false,
                contentType: false,
                processData: false,
                data: form_data,
                type: 'post',
                crossDomain: true,
                success: function(response){

                                document.getElementById("preview").src=response;

                                sessionStorage.urlImage = response;

                                document.getElementById("url_photo").value = response;
                }
      });
    }
    catch(e)
    {
      alert("error : " +  e);
     }
}
