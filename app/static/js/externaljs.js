
$(document).ready(function() {

	$("#owl-demo").owlCarousel({
   
        navigation : true, // Show next and prev buttons
        slideSpeed : 300,
        paginationSpeed : 400,
        singleItem:true,
        autoPlay : 5000
   
    });


    $("#owl-demo2").owlCarousel({
      items : 3,
      mouseDrag: true
      //itemsDesktop : [1199,3],
      //itemsDesktopSmall : [979,3]
 
    });


    $(".searchbar-open").click(function(){
          $(".menu").hide();
          //$(".searchbar").css({"display","none"});
          $(".searchbar-container").show();
          
    });


     $(".glyphicon-remove").click(function(){
          $(".menu").show();
          //$(".searchbar").css({"display","none"});
          $(".searchbar-container").hide();
          $(".account-container").hide();
          
    });


    $(".account-open").click(function(){
          $(".menu").hide();
          //$(".searchbar").css({"display","none"});
          $(".account-container").show();
          
    });

    $(".fa-bars").click(function(){
        $(".mobile-menu").show();  
    });

     $('.catalogue').click(function(){$('.main-menu-dropdown-panel').toggle(1000);});

     $('.headings li').click(function(){
        var tab_id = $(this).index()+1;
        $('.headings li').removeClass('active');
        $('.content li').removeClass('active');
        $(this).addClass('active');
        //$('.content li:'+'nth-child('+tab_id+')').addClass('active');
        $('.content li:nth-child('+tab_id+')').addClass('active');
     });


     // if($(document).width()<768){
     //  console.log('hello');
     // }

     $(window).resize(function(){

       if ($(window).width() <= 768) {
        $('.positions').removeClass('js');
        $('.positions').addClass('show-for-small');
       } 

       else if($(window).width() <= 1280){
        $('.positions').removeClass('js');
        $('.positions').addClass('show-for-medium-only');
        // $('.div').removeClass('positions show-for-medium-only');
        // $('.positions').addClass('show-for-large-up');
       }

       else{

        $('.positions').removeClass('js');
        $('.positions').addClass('positions show-for-large-up');
        // $('.positions').removeClass('positions show-for-small');
        // $('.positions').addClass('show-for-medium-only');
       }

    });

});

 
