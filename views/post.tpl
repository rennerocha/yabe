<div class="container">

  <div class="row">
    <div id="content" class="span10">
%if post:
      <h1>{{ post.title }}</h1>
      <h5 class="muted">{{ post.author }} - {{ post.date }}</h5>
      <hr/>
      <div id="post_content">
        {{ post.content }}
      </div>
%else:
      <h1>Nothing posted yet.</h1>
%end
    </div>
    <div class="span2">
      <a href="/archive/">ARCHIVE</a>
      <a href="https://github.com/rennerocha/yabe/">CÓDIGO-FONTE</a>
      <a href="/new/">NEW POST</a>
    </div>
  </div>

  <hr/>

  <div class="row">
    <div id="comments" class="span10">
      <h4>New comment</h4>
      <form method="post" action="/new/comment/">
      <input type="hidden" name="post_id" value="{{ post.id }}">
      <ul class="unstyled">
        <li><input type="text" name="author" placeholder="Author"></li>
        <li><textarea name="comment" placeholder="Your comment"></textarea></li>
      </ul>
      <input type="submit" value="Send Comment">
      </form>
      <h4>Comments</h4>
%for comment in post.comments:
      <div class="container">
      <p>Author: {{ comment.author }}</p>
      {{ comment.comment }}
      </div>
      <hr/>
%end
  </div>

</div>

%rebase base page_title=page_title
