const form = document.getElementById('contact-form');
const status = document.getElementById('status');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(event.target);

    try {
        const response = await fetch(event.target.action, {
            method: 'POST',
            body: formData,
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        });
        if (response.ok) {
            status.innerHTML = "Thanks for contacting us! We'll get back to you soon.";
            form.reset();
        } else {
            throw new Error('Network response was not ok.');
        }
    } catch (error) {
        status.innerHTML = "Oops! Something went wrong. Please try again later.";
    }
});
