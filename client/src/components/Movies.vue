<template>
    <div class="container">
      <div class="row">
        <div class="col-sm-10">
          <h1>Movies</h1>
          <hr><br><br>
          <button type="button" class="btn btn-success btn-sm">Add Movie</button>
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
             <tr>
               <td>foo</td>
               <td>bar</td>
               <td>baz</td>
               <td>foobarbaz</td>
               <td>
                 <button type="button" class="btn btn-warning btn-sm">Update</button>
                 <button type="button" class="btn btn-danger btn-sm">Delete</button>
               </td>
             </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
</template>

<script>
    export default {
        name: "Movies"
    }
</script>

<style scoped>

</style>
