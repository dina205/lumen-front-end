
const paymentForm = document.getElementById('payment-form');
paymentForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const formData = new FormData(paymentForm);
  const name = formData.get('name');
  const cardNumber = formData.get('card-number');
  const expiration = formData.get('expiration');
  const cvv = formData.get('cvv');
  const amount = formData.get('amount');
  const paymentData = {
    name,
    cardNumber,
    expiration,
    cvv,
    amount
  };
  const response = processPayment(paymentData);
  const receipt = generateReceipt(response);
  displayReceipt(receipt);
});
