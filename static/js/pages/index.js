/* --------- INDEX JS FILE --------- */

// FORM ELEMENTS
const travelFormEl = document.getElementById('App-form');
const dateOfTravelEl = document.getElementById('travel-date');
const dateOfReturnEl = document.getElementById('return-date');
const ageEl = document.getElementById('age');
const locationEl = document.getElementById('origin-country');
const destinationEl = document.getElementById('destination');

// RESULT ELEMENTS
const resultSectionEl = document.getElementById('result-section');
const resultTextEl = document.getElementById('result-text');
const resultImageEl = document.getElementById('result-img');
const resultWarningsEl = document.getElementById('result-warnings');

let eligibility = null;


const addWarning = (warning) => {
    resultWarningsEl.innerHTML += '・ ' + warning + '<br/>'
}


const goodResult = () => {
    resultImageEl.className = 'result-img'
    resultImageEl.src = '/static/media/confirm.svg';
    resultTextEl.innerText = 'You are eligble for travel';
}


const badResult = () => {
    resultImageEl.className = 'result-img'
    resultImageEl.src = '/static/media/decline.svg';
    resultTextEl.innerText = 'You are not eligble for travel';
}


const validateDateOfTravel = () => {
    const minimumDate = moment().add(1, 'days');
    const maximumDate = moment().add(6, 'days');
    const dateOfTravel = moment(dateOfTravelEl.value);

    if (minimumDate < dateOfTravel && maximumDate > dateOfTravel)
        return true;
    else
        addWarning('Date of travel must be within the next 2-5 working days.');

    return false;
};


const validateDateOfReturn = () => {
    const maximumDate = moment().add(2, 'months');
    const dateOfTravel = moment(dateOfTravelEl.value);
    const dateOfReturn = moment(dateOfReturnEl.value);

    if (!dateOfReturnEl.value)
        return true;

    if (dateOfReturn < dateOfTravel) {
        addWarning('Date of return must be later than date of travel');
        return false;
    }

    if (dateOfReturn < maximumDate)
        return true;
    else
        addWarning('Date of return must be within 2 months.');

    return false;
};


const validateAge = () => {
    const age = ageEl.value;

    if (21 <= age && age < 65) {
        return true;
    } else if (15 <= age && age < 21) {
        addWarning('You must have a supervising adult of atleast 21 years of age');
        return true;
    } else {
        addWarning('You must be between the age of 21 and 65 to travel');
    }

    return false;
}


const validateDestination = async () => {
    const loc = locationEl.value.replace(/ /g, "-");
    const des = destinationEl.value.replace(/ /g, "-");
    fetch(`/api/compare/${loc}/${des}`).then(
        res => {
            res.json().then(
                data => {
                    if (data[loc] < data[des] && eligibility) {
                        return goodResult();
                    } else {
                        if (data[loc] >= data[des]) {
                            addWarning(`Your current location is forbidden
                                from traveling to your selected destination`
                            );
                        }
                        return badResult();
                    }
                }
            )
        }
    )
}


const travelIsEligible = () => {

    // CONDITION 1: valid date of travel?
    if (!validateDateOfTravel()) eligibility = false;

    // CONDITION 2: valid date of return?
    if (!validateDateOfReturn()) eligibility = false;

    // CONDITION 3: valid age?
    if (!validateAge()) eligibility = false;

    // IF CONDITIONS 1 - 3 PASSED
    if (eligibility === null) eligibility = true;

    // CONDITION 4: valid location -> destination?
    validateDestination()
};


const onTravelFormSubmit = () => {
    travelFormEl.style.display = 'none';
    resultSectionEl.style.display = 'flex';
    resultImageEl.className = 'result-img-loading'
    resultImageEl.src = '/static/media/loading.svg';
    resultTextEl.innerText = 'loading...';
    travelIsEligible();
}
