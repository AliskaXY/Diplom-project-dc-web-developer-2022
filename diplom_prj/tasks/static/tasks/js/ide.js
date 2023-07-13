const testButton = document.getElementById("test");
const langSelector = document.getElementById("languages");
const url = window.location.href;
var language

$(document).ready(function() {
    language = $("#languages").val();
    getLastResult();
    langSelector.onchange = changeLanguage;
    testButton.onclick = executeCode;
});

$(document).ajaxStop(function() {
    editor = ace.edit("code-editor");
    solutionEditor = ace.edit("solution-editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode(getAceMode(language));
    $('#warningModalTaskSolution').on('shown.bs.modal', function (e) {
        solutionEditor.setTheme("ace/theme/monokai");
        solutionEditor.session.setMode(getAceMode(language))
    });
})

function getAceMode(language) {
    if (language === 'C' || language === 'CPP') {
        return "ace/mode/c_cpp";
    } else if (language === 'PHP') {
        return "ace/mode/php";
    } else if (language === 'PY') {
        return "ace/mode/python";
    } else if (language === 'JS') {
        return "ace/mode/javascript";
    }
}

function changeLanguage() {
    language = $("#languages").val();
    const get = '?language=' + language + '&solution-editor=need';
    const url = window.location.href + get;
    const ids = ['solution-editor'];
    ajaxRequest(url, ids, 'GET');
}

function getLastResult() {
    const get = '?language=' + language + '&code-editor=need&output=need&solution-editor=need';
    const url = window.location.href + get;
    const ids = ['code-editor', 'output', 'solution-editor'];
    ajaxRequest(url, ids, 'GET');
}

function executeCode() {
    const url = window.location.href + 'save';
    const ids = ['output'];
    let data = {
        language: language,
        code: editor.getSession().getValue()
    };
    ajaxRequest(url, ids, 'POST', data);
}

function ajaxRequest(url, ids, method, data=null) {
    const csrftoken = getCookie('csrftoken');
    const loadingMessage = 'Loading';
    let intervalId;
    let pointCount = 0;
    ids.forEach((item) => {
        if (item == 'output') {
          $('#'+item).empty()
            intervalId = setInterval(() => {
                const points = '.'.repeat(pointCount % 4);
                $('#'+item).html(`${loadingMessage}${points}`);
                pointCount++;
            }, 250);  
        }
    })    

    $.ajax({
        url: url,
        type: method,
        headers: { 'X-CSRFToken': csrftoken },
        cache: false,
        dataType: 'json',
        mode: 'same-origin',
        async: true,
        data: data,
        success: (response) => {
            ids.forEach((item) => {
                clearInterval(intervalId);
                $('#'+item).empty();
                if (response[item] != false) {
                    $('#'+item).html(response[item]);  
                } else {
                    $('#'+item).html('');
                }
            })    
        },
        error: function() {
            ids.forEach((item) => {
                clearInterval(intervalId);
                $('#'+item).empty();
                $('#'+item).html('An error occurred.');
            })    
        }
    })
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
