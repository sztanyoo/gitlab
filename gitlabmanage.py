import gitlab

# private token or personal token authentication
gl = gitlab.Gitlab('https://gitlab.example.com', private_token='KGduC4MT1rLYDB_BWTs5', ssl_verify=False)

# oauth token authentication
#gl = gitlab.Gitlab('http://10.0.0.1', oauth_token='my_long_token_here')

# job token authentication (to be used in CI)
import os
#gl = gitlab.Gitlab('http://10.0.0.1', job_token=os.environ['CI_JOB_TOKEN'])


# make an API request to create the gl.user object. This is mandatory if you
# use the username/password authentication.
gl.auth()

projects = gl.projects.list(all=True, retry_transient_errors=True)

for p in projects:
  print(p.name_with_namespace)
  issues = p.issues.list()
  for i in issues:
    print(i)
    issue = p.issues.get(i.iid)
    issue.labels = ['foo']
    issue.time_estimate('3h30m')

    issue.save()

    i_notes = issue.notes.list()
    for n in i_notes:
      print(n)
      if 2 == n.id:
        i_note = issue.notes.create({'body': 'mkey'})


