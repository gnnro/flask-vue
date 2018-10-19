<template>
    <div class="container">
      <div class="row">
        <div class="col-sm-10">
          <h1>Movies</h1>
          <hr><br><br>
          <alert :message="message" v-if="showMessage"></alert>
          <button type="button" class="btn btn-success btn-sm" v-b-modal.movie-modal>Add Movie
          </button>
          <br><br>
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Title</th>
                <th scope="col">Director</th>
                <th scope="col">Starring</th>
                <th scope="col">Watched?</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
             <tr v-for="(movie, index) in movies" :key="index">
               <td>{{ movie.title }}</td>
               <td>{{ movie.director }}</td>
               <td>{{ movie.starring }}</td>
               <td>
                 <span v-if="movie.watched">Yes</span>
                 <span v-else>No</span>
               </td>
               <td>
                 <button type="button" class="btn btn-warning btn-sm">Update</button>
                 <button type="button" class="btn btn-danger btn-sm">Delete</button>
               </td>
             </tr>
            </tbody>
          </table>
        </div>
      </div>
      <b-modal ref="addMovieModal" id="movie-modal" title="Add a new movie" hide-footer>
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-form-group id="form-title-group"
                        label="Title:"
                        label-for="form-title-input">
            <b-form-input id="form-title-input"
                          type="text"
                          v-model="addMovieForm.title"
                          required
                          placeholder="Enter title">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-director-group"
                        label="Director:"
                        label-for="form-director-input">
            <b-form-input id="form-director-input"
                          type="text"
                          v-model="addMovieForm.director"
                          required
                          placeholder="Enter director">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-starring-group"
                        label="Starring:"
                        label-for="form-starring-input">
            <b-form-input id="form-director-input"
                          type="text"
                          v-model="addMovieForm.starring"
                          required
                          placeholder="Enter actors">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-watched-group">
            <b-form-checkbox-group v-model="addMovieForm.watched" id="form-checks">
              <b-form-checkbox value="true">Watched?</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>
      </b-modal>
    </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert';

export default {
  data() {
    return {
      movies: [],
      addMovieForm: {
        title: '',
        director: '',
        starring: '',
        watched: [],
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getMovies() {
      const path = 'http://localhost:5000/movies';
      axios.get(path)
        .then((res) => {
          this.movies = res.data.movies;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addMovie(payload) {
      const path = 'http://localhost:5000/movies';
      axios.post(path, payload)
        .then(() => {
          this.getMovies();
          this.message = 'Movie added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getMovies();
        });
    },
    initForm() {
      this.addMovieForm.title = '';
      this.addMovieForm.director = '';
      this.addMovieForm.starring = '';
      this.addMovieForm.watched = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addMovieModal.hide();
      let watched = false;
      if (this.addMovieForm.watched[0]) watched = true;
      const payload = {
        title: this.addMovieForm.title,
        director: this.addMovieForm.director,
        starring: this.addMovieForm.starring,
        watched,
      };
      this.addMovie(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$ref.addMovieModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getMovies();
  },
};
</script>

<style scoped>

</style>
