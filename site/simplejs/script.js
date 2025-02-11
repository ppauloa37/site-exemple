    var contDown = document.getElementById("contdown1");
    
    var onContDown = function() {
        contDown.textContent = parseFloat(contDown.textContent) - 1
        
        
        
    };

    window.setInterval(onContDown, 1000);
