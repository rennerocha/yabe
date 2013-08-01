<div class="container">
  <div class="row">
  <h1>Archive</h1>
<ul>
%for post in posts:
<li><a href="/{{ post.date.year }}/{{ post.date.month }}/{{ post.slug }}">{{ post.title }} - ({{post.author }})</a></li>
%end
</ul>
  </div>
</div>

%rebase base page_title='Archive'
