

function showSpinner() {
    const spinner = document.getElementById('spinner');
    const overlay = document.getElementById('overlay');
    const content = document.getElementById('content');

    // Show the spinner and overlay
    spinner.style.visibility = 'visible';
    overlay.style.display = 'block';

    // Add blur effect to the content
    content.classList.add('blur');

    console.log('Spinner and overlay shown');

    // After 10 seconds (10000ms), hide the spinner and overlay
    setTimeout(function() {
        spinner.style.visibility = 'hidden';  // Hide the spinner
        overlay.style.display = 'none';  // Hide the overlay

        // Remove blur effect from the content
        content.classList.remove('blur');

        console.log('Spinner and overlay hidden');
    }, 10000);  // Set to 10 seconds (10000ms)

}





const observer = new IntersectionObserver ((entries)=>{

    entries.forEach((entry) => {

        console.log(entry)
        
        if(entry.isIntersecting){
            entry.target.classList.add('show');
        }
        
    });
});





const hiddenElemnt =document.querySelectorAll('.hidden');

hiddenElemnt.forEach((el) => observer.observe(el));