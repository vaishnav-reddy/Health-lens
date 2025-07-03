function handleSubmit(event) {
    event.preventDefault();
    
    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        message: document.getElementById('message').value
    };
    
    // Here you would typically send this data to a server
    console.log('Form submitted:', formData);
    
    // Clear the form
    event.target.reset();
    
    // Show success message
    alert('Thank you for your message! We will get back to you soon.');
} 