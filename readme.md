# Password Craking Assignmnets

This is a discription of 3 password cracking assignments. 

## Assignment One 1000 md5 Passwords to Crack


### Discription

For this practical, you have been emailed a list of 1000 password hashes and
are to solve those, finding the passwords for as many as you can.  Every hash
and password are unique - each of the (176,000!) passwords I generated is given
to just one student. If you haven't yet seen that mail, **first** check your
inbox and spam folders, and only then send a mail to Christian to check.

## Assignmnet Two 2000 mixed Password types to Crack

### Discription

For this practical, you will be emailed a list of 2000 password hashes and are
to solve those, finding the passwords for as many as you can.  Passwords are of
three different kinds this time, (i.e. selected in three different ways) and
six different hash functions are used. 

```
Give examples
```

## Assignment Three InfernoBall - Group Assignment

### Discription

This practical is intended as a digital analog to the rings of Dante's 
Inferno - you have to pass through each of the outer rings to get to the
centre, after which, you, like Dante, will be free to ascend to a higher plane
than this module:-)

This is a team assignment. As previously explained initial teams of 4
will be randomly selected from the set of students who have submitted
some file to submitty, that scored >0. (Submitting an empty file is
not sufficicent, if a badly formatted file was submitted that scored
zero but that contains broken passwords, that'll be allowed.)
Students who are not assigned to one of the initial teams will need
to contact me (Stephen Farrell) to explain why they've not submitted
anything and to be assigned a team.

For this practical, you will be emailed a file containing an "InfernoBall"
which is a nested data structure, in this case with 10 layers, that you need to
solve. (So not a tarball, but a bit like one.) Each layer contains:

- a set of password hashes
- a set of Shamir-like shares
- an encrypted version of the layer(s) below.

By solving the hashes you can get enough passwords to recover the secret key to
decrypt the next layer down.  And then you do that again 'till you reach the
lowest layer.

To get marks you need to submit a file with the recovered secrets succesfully
used for decryption. You'll get marks for each correct secret found. There are
some bonus marks for the first team to solve each layer, described below.


```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Hashcat

Talk about Hashcat

- Adv
- Disadv

## John the Ripper

Talk about John 

- Adv
- Disadv

```
Give an example
```

## AWS and Google Cloud

- Setup
- What ones where used and why
- Money Spent

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing


## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Stephen Kelehan** - *Initial work*


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
