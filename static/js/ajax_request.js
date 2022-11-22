$("#id_category").change(function () {
    var url = $("#techForm").attr("data-tech-url");  // Get the URL for retrieving technologies
    var categoryId = $(this).val();  // Get category 
    $.ajax({                       // Initialize AJAX Request
        url: url,                    // Set the above url
        data: {
            'category': categoryId       // Add Category's Id in the request
        },
        success: function (data) {
            $("#id_technology").html(data);  // Replace the content with the response received from request
        }
    });
});