const credit = document.querySelector('#credit');
const debit = document.querySelector('#debit');
const taksit = document.querySelector('#taksit');
const transfer = document.querySelector('#transfer');
const mastercard = document.querySelector('#mastercard');
const visa = document.querySelector('#visa');
const classic = document.querySelector('#classic');
const gold = document.querySelector('#gold');
const premium = document.querySelector('#premium');
const azn = document.querySelector('#azn');
const dollar = document.querySelector('#dollar');
const euro = document.querySelector('#euro');
const filter = document.querySelectorAll('#filter')


euro.addEventListener('click', () => {
    if (euro.style.backgroundColor != 'white') {
        euro.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('euro_f') === false) {
                e.classList.remove('d-none')
            }
        });
    } else {
        euro.style.backgroundColor = '#E1E3EF'
        dollar.style.backgroundColor = 'white'
        azn.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('euro_f') === false) {
                e.classList.add('d-none')
            }
        });
    }
});

dollar.addEventListener('click', () => {
    if (dollar.style.backgroundColor != 'white') {
        dollar.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('dollar_f') === false) {
                e.classList.remove('d-none')
            }
        });
    } else {
        dollar.style.backgroundColor = '#E1E3EF'
        azn.style.backgroundColor = 'white'
        euro.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('dollar_f') === false) {
                e.classList.add('d-none')
            }
        });
    }
});

azn.addEventListener('click', () => {
    if (azn.style.backgroundColor != 'white') {
        azn.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('azn_f') === false) {
                e.classList.remove('d-none')
            }
        });
    } else {
        azn.style.backgroundColor = '#E1E3EF'
        dollar.style.backgroundColor = 'white'
        euro.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('azn_f') === false) {
                e.classList.add('d-none')
            }
        });
    }
});

premium.addEventListener('click', () => {
    if (premium.style.backgroundColor != 'white') {
        premium.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('premium_f') === false) {
                e.classList.remove('d-none')
            }
        });
    } else {
        premium.style.backgroundColor = '#E1E3EF'
        gold.style.backgroundColor = 'white'
        classic.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('premium_f') === false) {
                e.classList.add('d-none')
            }
        });
    }
});

gold.addEventListener('click', () => {
    if (gold.style.backgroundColor != 'white') {
        gold.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('gold_f') === false) {
                e.classList.remove('d-none')
            }
        });
    } else {
        gold.style.backgroundColor = '#E1E3EF'
        classic.style.backgroundColor = 'white'
        premium.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('gold_f') === false) {
                e.classList.add('d-none')
            }
        });
    }
});

classic.addEventListener('click', () => {
    if (classic.style.backgroundColor != 'white') {
        classic.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('classic_f') === false) {
                e.classList.remove('d-none')
            }
        });
    } else {
        classic.style.backgroundColor = '#E1E3EF'
        gold.style.backgroundColor = 'white'
        premium.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('classic_f') === false) {
                e.classList.add('d-none')
            }
        });
    }
});

mastercard.addEventListener('click', () => {
    if (mastercard.style.backgroundColor != 'white') {
        mastercard.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('mastercard_f') === false) {
                e.classList.remove('d-none')
            }
        });
    } else {
        mastercard.style.backgroundColor = '#E1E3EF'
        visa.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('mastercard_f') === false) {
                e.classList.add('d-none')
            }
        });
    }
});

visa.addEventListener('click', () => {
    if (visa.style.backgroundColor != 'white') {
        visa.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('visa_f') === false) {
                e.classList.remove('d-none')
            }
        });
    } else {
        visa.style.backgroundColor = '#E1E3EF'
        mastercard.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('visa_f') === false) {
                e.classList.add('d-none')
            }
        });
    }
});

credit.addEventListener('click', () => {
    if (credit.style.backgroundColor != 'white') {
        credit.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('credit_f') === false) {
                e.classList.remove('d-none')
            }
        });
    } else {
        credit.style.backgroundColor = '#E1E3EF'
        debit.style.backgroundColor = 'white'
        taksit.style.backgroundColor = 'white'
        transfer.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('credit_f') === false) {
                e.classList.add('d-none')
            }
        });
    }
});

debit.addEventListener('click', () => {
    if (debit.style.backgroundColor != 'white') {
        debit.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('debit_f') === false) {
                e.classList.remove('d-none')
            }
        });
    } else {
        debit.style.backgroundColor = '#E1E3EF'
        credit.style.backgroundColor = 'white'
        taksit.style.backgroundColor = 'white'
        transfer.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('debit_f') === false) {
                e.classList.add('d-none')
            }
        });
    }});

taksit.addEventListener('click', () => {
    if (taksit.style.backgroundColor != 'white') {
        taksit.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('taksit_f') === false) {
                e.classList.remove('d-none')
            }
        });
    } else {
        taksit.style.backgroundColor = '#E1E3EF'
        debit.style.backgroundColor = 'white'
        transfer.style.backgroundColor = 'white'
        credit.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('taksit_f') === false) {
                e.classList.add('d-none')
            }
        });
    }
});

transfer.addEventListener('click', () => {
    if (transfer.style.backgroundColor != 'white') {
        transfer.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('transfer_f') === false) {
                e.classList.remove('d-none')
            }
        });
    } else {
        transfer.style.backgroundColor = '#E1E3EF'
        debit.style.backgroundColor = 'white'
        credit.style.backgroundColor = 'white'
        taksit.style.backgroundColor = 'white'
        filter.forEach(e => {
            if (e.classList.contains('transfer_f') === false) {
                e.classList.add('d-none')
            }
        });
    }
});
