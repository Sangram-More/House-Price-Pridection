const form = document.querySelector('form');
const submitButton = document.querySelector('button[type="submit"]');
const image = document.querySelector('#image');

form.addEventListener('submit', function (event) {
    event.preventDefault();
    const dataset = document.getElementById('input[name="Choose a Dataset":checked').value;
    const model = document.getElementById('input[name="Choose a Model":checked').value;
    const crossValidation = document.querySelector('input[name="Cross- Validation"]:checked').value;

    // Update the image source based on user input
    if (dataset === 'India CSV File' && crossValidation === 'yes' && model === "Linear Regression") {
        image.src = 'D:\College\SEM - 8\BE Final project\Front-End Web Pages\Cross-Validation\Linear Regression.png';
    } else if (dataset === 'India CSV File' && crossValidation === 'no' && model === 'Linear Regression') {
        image.src = 'D:\College\SEM - 8\BE Final project\Front-End Web Pages\Normal\Linear Regression-N.png';
    } else if (dataset === 'India CSV File' && crossValidation === 'yes' && model === 'Ridge Regression') {
        image.src = 'D:\College\SEM - 8\BE Final project\Front-End Web Pages\Cross-Validation\Ridge Regression.png';
    } else if (dataset === 'India CSV File' && crossValidation === 'no' && model == 'Ridge Regression') {
        image.src = 'D:\College\SEM - 8\BE Final project\Front-End Web Pages\Normal\Ridge Regression-N.png';
    } else if (dataset === 'India CSV File' && crossValidation === 'yes' && model == 'Lasso Regression') {
        image.src = 'D:\College\SEM - 8\BE Final project\Front-End Web Pages\Cross-Validation\Lasso Regression.png';
    } else if (dataset === 'India CSV File' && crossValidation === 'no' && model == 'Lasso Regression') {
        image.src = 'D:\College\SEM - 8\BE Final project\Front-End Web Pages\Normal\Lasso Regression-N.png';
    }
    imageContainer.appendChild(image);
});


