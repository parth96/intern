// Class Inssurance.
class Insurance{
    constructor(brand,model,year, type){
        this.brand = brand;
        this.model = model;
        this.year = year;
        this.type = type;
    }
   
// function generateQuote
 generateQuote() {

    /*
    Brand
      Ford 1.15
      Honda 1.05
      Audi 1.35

    Model
      Hatchback 1.10
      Sedan     1.13
      Cabriolet 1.20
      SUV       1.15
    */

    let value;
    const base  = 2000;

    switch(this.brand){
        case "Ford":
        value = base * 1.15;
        break;
        case "Honda":
        value = base * 1.05;
        break;
        case "Audi":
        value = base * 1.35;
        break;
    }


    switch(this.model){
        case "Hatchback":
        value *= 1.10;
        break;
        case "Sedan":
        value *= 1.13;
        break;
        case "Cabriolet":
        value *= 1.20;
        break;
        case "SUV":
        value *= 1.15
        break;
    }
    
    //read year.
    const difference = new Date().getFullYear() - this.year;
    //Each year the difference redice by 3% the value.
    value -= ((difference * 3)* value)/100;

    /*If the insurance is basic it will be multiply by 30% more.
      If the insurance is complete it wll be multiply by 50% more.
      */
     if(this.type == 'basic'){
         value*= 1.30;
     }else {
         value*= 1.50;
     }
    return value;
 }

}

//Class Interface.
class Interface{

 //Function showMessage (error or generating)   
 showMessage(message, type){
    const div = document.createElement('div');
    if (type === 'error'){
        div.classList.add('message','error');
    } else {
        div.classList.add('message','correct');
    }
    div.innerHTML = `${message}`;
    form.insertBefore(div,document.querySelector('.form-group'));

    setTimeout(function(){
      document.querySelector('.message').remove();
    },3000);
}
// Function Result message.
showResult(insurance, total){
    const result = document.getElementById('result');

    const div = document.createElement('div');
    div.innerHTML = `
     <p class = 'header':>Your Insurance Details:</p>
    <p>Brand: ${insurance.brand}</p>
    <p>Model: ${insurance.model}</p>
    <p>Year: ${insurance.year}
    <p>Type: ${insurance.type}
    <p>Total: $ ${total}
    `;
    const spinner = document.querySelector('#loading');
    spinner.style.display = 'block';
    console.log(spinner);
    setTimeout(function(){
     spinner.style.display ='none';
     result.appendChild(div);
    },3000);
 }

}
 
//event listeners(submit event) and making instance classes
const form = document.getElementById('quoteForm');
form.addEventListener('submit', function(e){
 e.preventDefault();

 //Read selected brand.
 const brand = document.getElementById('brand');
 const brandSelection = brand.options[brand.selectedIndex].value;

 //Read selected model.
 const model = document.getElementById('model');
 const modelSelection = model.options[model.selectedIndex].value;
 
 //Read Selected year.
 const year = document.getElementById('year');
 const yearSelection = year.options[year.selectedIndex].value;

 //Read radio button.
 const type = document.querySelector('input[name="type"]:checked').value;

 //Instantiate Interface class.
 const interface = new Interface();

 //checks if there is not empty data in form.
 if(brandSelection == '' || modelSelection =='' || yearSelection == '' || type == ''){
    //Using interface method
    interface.showMessage('Some data is missing, check the form again please', 'error');
 } else {
    //Clean old results.
    const result = document.querySelector('#result div');
    if(result != null){
        result.remove();
    }

   //Instantiate Insurance class
    const insurance = new Insurance(brandSelection, modelSelection, yearSelection, type);
    //Generating quote.
    const total = insurance.generateQuote();
    //Show Result.
    interface.showResult(insurance,total);
    interface.showMessage('Generating...', 'correct')
 }
});

// Fill the form with the years in the year select.
const max = new Date().getFullYear();
        min = max-20;

const selectYears= document.getElementById('year');

for(let i = max; i>=min; i--){
    let option = document.createElement('option');
    option.value = i;
    option.innerHTML = i;
    selectYears.appendChild(option);
}