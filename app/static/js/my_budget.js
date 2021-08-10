$(document).ready(function() {
    $('#inter5').click(function (e){
        c = $('#nam5').val()
        x = c.length
        v = $('#pas5').val()
        i = v.length
        if (x < 5) {
            alert('Логин меньше 5 символов');
            return false;
        }
        if (i < 5) {
            alert('Пароль меньше 5 символов');
            return false;
        }
    })
    $('#sub1').click(function (e){
        l = $('#log1').val()
        l1 = l.length
        p = $('#pas1').val()
        p1 = p.length
        n = $('#nam1').val()
        n1 = n.length
        nn = $('#nam2').val()
        n2 = nn.length
        em = $('#email1').val()
        em1 = em.length
        if (l1 < 5) {
            alert('Логин меньше 5 символов');
            return false;
        }
        if (p1 < 5) {
            alert('Пароль меньше 5 символов');
            return false;
        }
        if (n1 < 2) {
            alert('Имя меньше 2 символов');
            return false;
        }
        if (n2 < 2) {
            alert('Фамилия меньше 2 символов');
            return false;
        }
        if (em1 < 6) {
            alert('Email слишком короткий');
            return false;
        }
    })

    $('#log1').blur(function (){
        $.post(
        'log_2',
            {'aaa': $('#log1').val()},
            function (response) {
                if (response.exists == 'y' ) {
                    alert('Такой пользователь уже есть')
                }
            }
        )
    })
});