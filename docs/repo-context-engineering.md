# Repo context engineering

Bad agent output often starts with bad context. Too many files confuse the model. Too few files make it invent glue. The trick is to package the part of the repo that controls behavior, then add constraints and tests.

A good context brief answers five questions: what should change, what must not change, which files decide behavior, which tests prove it, and what a rollback would look like.
