const RelevantResults = Vue.component('relevant-results', {
    props: {
        responseData: Array,
        loading: Boolean,
        method: Function
    },
    template: `
<div class="row" :class="{ 'isLoading': loading }" v-if="responseData">
                        <div class="col">
                            <div class="table-responsive">
                                <table class="table table-dark">
                                    <thead>
                                    <tr>
                                        <th>Related Questions</th>
                                        <th>Score</th>
                                    </tr>
                                    </thead>
                                    <tbody>

                                    <tr v-for="(item, index) in responseData">
                                        <td><a href="javascript:void(0)"
                                               @click="mymethod(item[0])">{{ item[0] }}</a></td>
                                        <td>
                                            <small><i class="text-info">{{ item[2] }}</i></small>
                                        </td>
                                    </tr>
                                    </tbody>
                                </table>

                            </div>
                        </div>
                    </div>
  `,
    methods: {
        mymethod(value) {
            this.method(value)
        }
    }
});

const Foo = {template: '<div></div>'};

const routes = [
    {path: '/search', component: RelevantResults},
    {path: '/', component: RelevantResults},
    {path: '/upload', component: Foo},
];

const router = new VueRouter({
    routes // short for `routes: routes`
});

Vue.directive('linkified', function (el, binding) {
    linkifyElement(el, binding.value);
});

const RFP_BOT = {
    router,
    el: "#counter",
    data() {
        return {
            question: '',
            answer: '',
            relevantQ: '',
            relevantA: '',
            relevantQScore: 0,
            responseData: '',
            jwt: '',
            username: '',
            password: '',
            errorMessage: '',
            loading: false
        }
    },
    methods: {
        logout() {
            this.jwt = '';
            localStorage.jwt = '';
        },
        search() {
            router.push({path: 'search', query: {question: this.question}});
            console.log(this.question)
            if (this.question && 0 !== this.question.trim().length) {
                this.loading = true;
                const headers = {
                    headers: {
                        'Authorization': "JWT " + this.jwt
                    }
                };
                axios.get('http://10.51.101.102:8080/?question=' + this.question, headers).then(
                    response => (
                        this.loading = false,
                            this.relevantQ = response['data'][0][0],
                            this.relevantA = response['data'][0][1],
                            this.relevantQScore = response['data'][0][2],
                            this.relevantQSupported = response['data'][0][3],
                            this.relevantQCategory = response['data'][0][4],
                            this.relevantQSubCategory = response['data'][0][5],
                            this.responseData = response['data'].slice(1))
                ).catch(error => {
                    this.errorMessage = error.message;
                    this.jwt = '';
                    this.loading = false;
                    console.error("There was an error!", error);
                });
            }

        },
        handleLinkClick(item) {
            this.question = item;
            this.search();
            window.scrollTo(0, 0);
        },
        submitLoginForm(e) {
            e.preventDefault();
            const credentials = {username: this.username, password: this.password};
            this.errorMessage = '';
            axios.post("http://10.51.101.102:8080/auth", credentials)
                .then(response => (this.jwt = response.data.access_token, localStorage.jwt = response.data.access_token))
                .catch(error => {
                    this.errorMessage = error.message;
                    console.error("There was an error!", error);
                });
        }
    },
    mounted() {
        if (localStorage.jwt) {
            this.jwt = localStorage.jwt;
        }
        if (this.$route.query.question !== '') {
            this.question = this.$route.query.question;
            this.search();
        }
    },
};

const app = new Vue(RFP_BOT);