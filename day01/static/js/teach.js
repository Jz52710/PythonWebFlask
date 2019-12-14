$(function () {
    let edit = $('.edit');
    edit.click(function () {//更改
        let tr =$(this).parents("tr");
        let children = tr.children("td");
        $('.tj-box').fadeIn();//显示
        console.log($(this))
        console.log(tr)
        console.log(children)
        let id = children.eq(0).text();
        $('#up').attr('sid',id)
        $('[name=name]').val(children.eq(1).text());
        $('[name=num]').val(children.eq(2).text());
        if (children.eq(3).attr('val') == 1) {
            console.log(123)
            $('[name=sex]').eq(0).attr('checked','checked')
        }else {
            console.log(2)
            $('[name=sex]').eq(1).attr('checked','checked')
        }
        $('[name=job]').val(children.eq(4).text());
        $('[name=tall]').val(children.eq(5).text());
        console.log(children.eq(3).attr('val'))
    });

    $('#up').click(function () {
        $.ajax({
            url:'edit',
            type:'post',
            data:{
                id:$('#up').attr('sid'),
                name:$("[name=name]").val(),
                num:$("[name='num']").val(),
                sex:$("[name=sex]").val(),
                job:$("[name=job]").val(),
                tall:$("[name=tall]").val(),
            },
            success:function (data) {
                console.log(data);
                $('.tj-box').fadeOut()
            },
            error:function (e) {
                console.log(e)
            }
        })
    })
})