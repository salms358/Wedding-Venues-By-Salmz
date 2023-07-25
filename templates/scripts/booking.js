function formValidation() {
    const nInput = document.getElementsByName('customer-name');
    const eInput = document.getElementsByName('email');
    const dInput = document.getElementsByName('booking_date');

    if (nInput.value.trim() === '') {
        alert("Please enter you name")
        return false;
    }
    if (eInput.value.trim)() === '' {
        alert('please enter in your email')
        return false;
    }
}
 