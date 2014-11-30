from openerp import http


class Academy(http.Controller):
    @http.route('/academy/', auth='public', website=True)
    def index(self):
        Teachers = http.request.env['academy.teachers']
        return http.request.render('academy.index', {'teachers': Teachers.search([])})

    @http.route('/academy/<model("academy.teachers"):teacher>/', auth='public', website=True)
    def teacher(self, teacher):
        return http.request.render('academy.biography', {
            'person': teacher
        })
