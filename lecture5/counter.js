let counter = 0;
function count() {
    
    counter++;
    document.querySelector('h1').innerHTML = counter;
    

    if(counter % 10 === 0)
    {
        alert(`Now counter is ${counter}`);
    }
  
}
    document.addEventListener('DOMContentLoaded', function() { // loading the whole page before calling count function
                    //anonymous function
            document.querySelector('button').onclick=count; // assigning a function to a variable
            
            document.querySelector('form').onsubmit = function() {
                const name = document.querySelector('#name').value;
                alert(`Hello, ${name}`);
            };
        });
        
