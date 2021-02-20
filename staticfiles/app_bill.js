function get_data(){
		
	    $.ajax({
			url : "/bill/view/?key="+$("#search").val(), 
			dataType: 'json',
			success: function(data) {
				console.log(data[0].dennis);
				var k = 0;
				var tot = 0;
				var th,option_val = "";
				for(var i of data[0].dennis) {
					option_val += "<option value='"+i.fields.company_code+"'>"+i.fields.company_code+" - "+i.fields.company_name+"</option>";
					}
				$("#company_code").html(option_val);	
				for(var j of data[0].dita.pickups) {
					k++;
					//can use break;
					tot += parseInt(j[4]);
					th += "<tr><th>"+k+"</th>";
					th += "<th><button class='btn btn-info' onclick='response_edit("+j[0]+")'>Edit</button> <button onclick='response_del("+j[0]+")' class='btn btn-danger'>Delete</button></th>";
					th += "<th>"+j[1]+" - "+j[2]+"</th>";
					th += "<th>"+j[3]+"</th>";
					th += "<th style='text-align:right'>"+j[4].toLocaleString()+"</th></tr>";
					}	
					th += "<tr><th colspan=5 style='text-align:right'> Total : "+tot.toLocaleString()+"</th></tr>";
				$("#table_content > tbody").html(th);

			}
	   });
}

		
function response_del(id){
 		$.ajax({
	    url : "/bill/delete/"+id,
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
			url : '/bill/get/'+id,
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
	
	$("#search_btn").click(function(e){
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
            url: "/bill/save/",
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