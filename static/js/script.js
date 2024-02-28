// SELECT ALL / DESELECT ALL CHECKBOXES BUTTONS

// General Attributes checkboxes
var buttonResetAttributes = document.getElementById('button-reset-attributes')
buttonResetAttributes.addEventListener('click', resetAttributes)
var attributesSelected = true;

function resetAttributes() {

    if (attributesSelected === true) {
        document.getElementById('checkbox-first-initial').checked = false;
        document.getElementById('checkbox-last-initial').checked = false;
        document.getElementById('checkbox-alignment').checked = false;
        document.getElementById('checkbox-race').checked = false;
        document.getElementById('checkbox-class').checked = false;
        attributesSelected = false;
        buttonResetAttributes.innerText = 'Select All';
    }
    else {
        document.getElementById('checkbox-first-initial').checked = true;
        document.getElementById('checkbox-last-initial').checked = true;
        document.getElementById('checkbox-alignment').checked = true;
        document.getElementById('checkbox-race').checked = true;
        document.getElementById('checkbox-class').checked = true;
        attributesSelected = true;
        buttonResetAttributes.innerText = 'Deselect All';
    }
}

// Race checkboxes
var buttonResetRaces = document.getElementById('button-reset-races')
buttonResetRaces.addEventListener('click', resetRaces)
var racesSelected = true;

function resetRaces() {

    if (racesSelected === true) {
        document.getElementById('checkbox-race-Dragonborn').checked = false;
        document.getElementById('checkbox-race-Dwarf').checked = false;
        document.getElementById('checkbox-race-Elf').checked = false;
        document.getElementById('checkbox-race-Gnome').checked = false;
        document.getElementById('checkbox-race-Half-Elf').checked = false;
        document.getElementById('checkbox-race-Halfling').checked = false;
        document.getElementById('checkbox-race-Half-Orc').checked = false;
        document.getElementById('checkbox-race-Human').checked = false;
        document.getElementById('checkbox-race-Tiefling').checked = false;
        racesSelected = false;
        buttonResetRaces.innerText = 'Select All';
    }
    else {
        document.getElementById('checkbox-race-Dragonborn').checked = true;
        document.getElementById('checkbox-race-Dwarf').checked = true;
        document.getElementById('checkbox-race-Elf').checked = true;
        document.getElementById('checkbox-race-Gnome').checked = true;
        document.getElementById('checkbox-race-Half-Elf').checked = true;
        document.getElementById('checkbox-race-Halfling').checked = true;
        document.getElementById('checkbox-race-Half-Orc').checked = true;
        document.getElementById('checkbox-race-Human').checked = true;
        document.getElementById('checkbox-race-Tiefling').checked = true;
        racesSelected = true;
        buttonResetRaces.innerText = 'Deselect All';
    }
}

// Class checkboxes
var buttonResetClasses = document.getElementById('button-reset-classes')
buttonResetClasses.addEventListener('click', resetClasses)
var classesSelected = true;

function resetClasses() {

    if (classesSelected === true) {
        document.getElementById('checkbox-class-Barbarian').checked = false;
        document.getElementById('checkbox-class-Bard').checked = false;
        document.getElementById('checkbox-class-Cleric').checked = false;
        document.getElementById('checkbox-class-Druid').checked = false;
        document.getElementById('checkbox-class-Fighter').checked = false;
        document.getElementById('checkbox-class-Monk').checked = false;
        document.getElementById('checkbox-class-Paladin').checked = false;
        document.getElementById('checkbox-class-Ranger').checked = false;
        document.getElementById('checkbox-class-Rogue').checked = false;
        document.getElementById('checkbox-class-Sorcerer').checked = false;
        document.getElementById('checkbox-class-Warlock').checked = false;
        document.getElementById('checkbox-class-Wizard').checked = false;
        classesSelected = false;
        buttonResetClasses.innerText = 'Select All';
    }
    else {
        document.getElementById('checkbox-class-Barbarian').checked = true;
        document.getElementById('checkbox-class-Bard').checked = true;
        document.getElementById('checkbox-class-Cleric').checked = true;
        document.getElementById('checkbox-class-Druid').checked = true;
        document.getElementById('checkbox-class-Fighter').checked = true;
        document.getElementById('checkbox-class-Monk').checked = true;
        document.getElementById('checkbox-class-Paladin').checked = true;
        document.getElementById('checkbox-class-Ranger').checked = true;
        document.getElementById('checkbox-class-Rogue').checked = true;
        document.getElementById('checkbox-class-Sorcerer').checked = true;
        document.getElementById('checkbox-class-Warlock').checked = true;
        document.getElementById('checkbox-class-Wizard').checked = true;
        classesSelected = true;
        buttonResetClasses.innerText = 'Deselect All';
    }
}


// GENERATE CHARACTER BUTTON
var buttonGenerateCharacter = document.getElementById('button-generate-character')
buttonGenerateCharacter.addEventListener('click', sendSettings);

function sendSettings() {

    // Get checkbox states: Attributes
    var firstInitialChecked = document.getElementById('checkbox-first-initial').checked;
    var lastInitialChecked = document.getElementById('checkbox-last-initial').checked;
    var alignmentChecked = document.getElementById('checkbox-alignment').checked;
    var raceChecked = document.getElementById('checkbox-race').checked;
    var classChecked = document.getElementById('checkbox-class').checked;
    
    // Get checkbox states: Races
    var checkedRaces = [];
    document.querySelectorAll('input[name^="checkbox-race-"]:checked').forEach(function(checkbox) {
        // Find the associated label which is immediately before the checkbox
        var label = checkbox.previousElementSibling;
        // Ensure that the found element is indeed a label e.g. 'Dwarf'
        if (label && label.tagName === 'LABEL') {
            // Add the label e.g. 'Dwarf' to the list of checked classes
            checkedRaces.push(label.textContent || label.innerText);
        }
    });
    console.log("Checked races:", checkedRaces);
    // Handle no checked races
    if (checkedRaces.length === 0) {
        checkedRaces.push("None")
    }

    // Get checkbox states: Classes
    var checkedClasses = [];
    document.querySelectorAll('input[name^="checkbox-class-"]:checked').forEach(function(checkbox) {
        // Find the associated label which is immediately before the checkbox
        var label = checkbox.previousElementSibling;
        // Ensure that the found element is indeed a label e.g. 'Barbarian'
        if (label && label.tagName === 'LABEL') {
            // Add the label e.g. 'Barbarian' to the list of checked classes
            checkedClasses.push(label.textContent || label.innerText);
        }
    });
    console.log("Checked classes:", checkedClasses);
    // Handle no checked classes
    if (checkedClasses.length === 0) {
        checkedClasses.push("None")
    }

    // Get GPT settings
    var gptNameChecked = document.getElementById('checkbox-gpt-name').checked;
    var genderSelected = document.getElementById('dropdown-gender').value;
    var genreSelected = document.getElementById('dropdown-genre').value;

    // Send AJAX request to Flask backend
    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            firstInitialChecked: firstInitialChecked,
            lastInitialChecked: lastInitialChecked,
            alignmentChecked: alignmentChecked,
            raceChecked: raceChecked,
            classChecked: classChecked,

            checkedRaces: checkedRaces,
            checkedClasses: checkedClasses,
            
            gptNameChecked: gptNameChecked,
            genreSelected: genreSelected,
            genderSelected: genderSelected
        })
    })
    .then(response => response.json())
    .then(data => {
        // Update the webpage with the generated initials
        // document.getElementById('first-initial').textContent = data.first_initial;
        // document.getElementById('last-initial').textContent = data.last_initial;
        document.getElementById('input-first-name').value = data.first_initial;
        document.getElementById('input-last-name').value = data.last_initial;
        document.getElementById('alignment').textContent = data.alignment;
        document.getElementById('race').textContent = data.race;
        document.getElementById('class').textContent = data.class;
        document.getElementById('gpt-name').textContent = data.gpt_name;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


// REROLL ATTRIBUTES
function rerollAttribute(attributeName){
    
    console.log("Reroll attribute.");

    // Send AJAX request to Flask backend
    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'reroll-attribute': attributeName
        })
    })
    .then(response => response.json())
    .then(data => {
        // Update the webpage with the generated initials
        // document.getElementById('first-initial').textContent = data.first_initial;
        // document.getElementById('last-initial').textContent = data.last_initial;
        document.getElementById('input-first-name').value = data.first_initial;
        document.getElementById('input-last-name').value = data.last_initial;
        document.getElementById('alignment').textContent = data.alignment;
        document.getElementById('race').textContent = data.race;
        document.getElementById('class').textContent = data.class;
    })
    .catch(error => {
        console.error('Error:', error);
    });

}


// REACTIVE CHARACTER SHEET BEHAVIOUR
var gptNameCheckbox = document.getElementById('checkbox-gpt-name');
gptNameCheckbox.addEventListener('click', alterCharacterSheet);

function alterCharacterSheet(){
    
    if (gptNameCheckbox.checked) {
        // Hide First Initial and Last Initial 
        document.getElementById('first-name').style.display = 'none';
        document.getElementById('last-name').style.display = 'none';
        // Show Full Name
        document.getElementById('p-gpt-name').style.display = 'block';

    } else {
        // Show First Initial and Last Initial
        document.getElementById('first-name').style.display = 'block';
        document.getElementById('last-name').style.display = 'block';

        // Hide Full Name
        document.getElementById('p-gpt-name').style.display = 'none';
    }
}


// SENDING USER-INPUTTED NAMES TO BACKEND
document.addEventListener("DOMContentLoaded", function(){

    const inputFirstName = document.getElementById("input-first-name");
    const inputLastName = document.getElementById("input-last-name");
    let originalFirstName = inputFirstName.value;
    let originalLastName = inputLastName.value;

    // When the input field gains focus, store the current value 
    inputFirstName.addEventListener('focus', function(){ 
        originalFirstName = inputFirstName.value;
    })
    inputLastName.addEventListener('focus', function(){ 
        originalLastName = inputLastName.value;
    })

    // When focus is lost, check if the value has changed
    inputFirstName.addEventListener('blur', function() {
        // If the value has changed, send the data
        if (inputFirstName.value !== originalFirstName) {
            sendFirstName(inputFirstName.value);
        }
    })
    inputLastName.addEventListener('blur', function() {
        // If the value has changed, send the data
        if (inputLastName.value !== originalLastName) {
            sendLastName(inputLastName.value);
        }
    })

    // If Enter key is pressed, check if the value has changed
    inputFirstName.addEventListener('keypress', function(event) {
        if (event.key === 'Enter' && inputFirstName.value !== originalFirstName) {
            event.preventDefault(); // Prevent the default action to avoid form submission or other unwanted behaviour
            sendFirstName(inputFirstName.value);
        }
    })
    inputFirstName.addEventListener('keypress', function(event) {
        if (event.key === 'Enter' && inputLastName.value !== originalLastName) {
            event.preventDefault(); // Prevent the default action to avoid form submission or other unwanted behaviour
            sendLastName(inputLastName.value);
        }
    })


    function sendFirstName(name) {

        console.log("Sending data:", name); // Placeholder for AJAX call

        fetch('/save-first-name', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ inputFirstName: name }),
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch((error) => {
            console.error('Error:', error);
        })
    }

    function sendLastName(name) {

        console.log("Sending data:", name); // Placeholder for AJAX call

        fetch('/save-last-name', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ inputLastName: name }),
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch((error) => {
            console.error('Error:', error);
        })
    }
})


// GENERATE PORTRAIT IMAGE
var buttonGeneratePortrait = document.getElementById('button-generate-image')
buttonGeneratePortrait.addEventListener('click', generateImage);

function generateImage() {

    buttonGeneratePortrait.disabled = true;
    buttonGeneratePortrait.style.backgroundColor = 'grey';
    buttonGeneratePortrait.textContent = "Generating Portrait...";

    // Get information needed for image generation
    var genreSelected = document.getElementById('dropdown-genre').value;
    var genderSelected = document.getElementById('dropdown-gender').value;
    var gptName = document.getElementById('gpt-name').textContent;
    var alignment = document.getElementById('alignment').textContent;
    var race = document.getElementById('race').textContent;
    var class_ = document.getElementById('class').textContent;

    console.log('genreSelected:', genreSelected);
    console.log('genderSelected:', genderSelected);
    console.log('gptName:', gptName);
    console.log('alignment:', alignment);
    console.log('race:', race);
    console.log('class_:', class_);


    fetch('/generate-image', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'genre': genreSelected,
            'gender': genderSelected,
            'gpt_name': gptName,
            'alignment': alignment,
            'race': race,
            'class': class_
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        // Replace src attribute of image 
        document.getElementById('gpt-image').src = data.imageUrl;
        buttonGeneratePortrait.disabled = false;
        buttonGeneratePortrait.style.backgroundColor = '';
        buttonGeneratePortrait.textContent = "Generate Portrait";
    })
    .catch((error) => {
        console.error('Error:', error);
        // Handle errors here
        buttonGeneratePortrait.disabled = false;
        buttonGeneratePortrait.style.backgroundColor = '';
        buttonGeneratePortrait.textContent = "Generate Portrait";
    });
}