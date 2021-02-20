function get_data(){
		
	    $.get("/company/view/?key="+$("#search").val(), function(data) {
			var k = 0;
			var th = "";
			for(var i of data) {
				k++;
				//can use break;
				th += "<tr><th>"+k+"</th>";
				th += "<th><button class='btn btn-info' onclick='response_edit("+i.pk+")'>Edit</button> <button onclick='response_del("+i.pk+")' class='btn btn-danger'>Delete</button></th>";
				th += "<th>"+i.fields.company_code+"</th>";
				th += "<th>"+i.fields.company_name+"</th>";
				th += "<th>"+i.fields.phone_number+"</th>";
				th += "<th>"+i.fields.address+"</th></tr>";
			}
			$("#table_content > tbody").html(th);
		});
	}

		
function response_del(id){
 		$.ajax({
	    url : "/company/delete/"+id,
	    type: "GET",
	    success: function(data)
	    {  
	    	$('#company_submit').trigger("reset")
			$("#company_code").attr("readonly",false);	
			$("#company_code").focus();
	    }
		}).done(function() {
			get_data()});		
		
}	

function response_edit(id)
{
		$.ajax({
			url : '/company/get/'+id,
			type: 'GET',
			success: function(data)
			{
				 $.each( data[0].fields, function( key, value ) {
					  $("#"+key).val(value);
				});
				
				$("#id").val(data[0].pk);
				
				$("#company_code").attr("readonly","readonly");
				 
				
			}
		})
}
	
	
$(document).ready(function() {
	
	
	$("#company_code").focus();
	
    get_data();
	
	$("#search").keyup(function(e){
	   get_data();
    });
	
    $('#add_save').click(function(e) {
		var errors = 0;
		$("#company_submit :input").map(function(){
			 if( !$(this).val() ) {
				  $(this).parents('td').addClass('warning');
				  errors++;
			} else if ($(this).val()) {
				  $(this).parents('td').removeClass('warning');
			}   
		});
		if(errors > 0){
			alert("All fields are required")
			return false;
		}
	
        $.ajax({
            url: "/company/save/",
	        type: "POST",
            data: $('#company_submit').serialize()+"&id="+$("#id").val(),
            success: function(data, status, xhr) {
				$('#company_submit').trigger("reset")
				$("#company_code").attr("readonly",false);	
				$("#company_code").focus();
            }
        }).done(function() {
			get_data()})
	});
	
	$('.edit').click(function() {

	
	}); // edit close
});