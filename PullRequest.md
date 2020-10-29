                                               ABOUT HACKTOBER FEST
                            Open Source is changing the world - one Pull Request at a time! 

***HacktoberFest*** is a month long celebration in October (as the name suggests) every year. It is for the millions of people who either contribute or are willing to contribute to open source. This is run by DigitalOcean in partnership with GitHub and Twilio. Hacktoberfest is open to everyone in our global community!

You need to make minimum of **4 pull requests** to contribute to open source. The first 70,000 valid PRs are considered. If your PR counts for a valid one, you are one step closer to achieve HacktoberFest Swags and HacktoberFest T-shirt.

Below are the steps to create a pull request.

1. Fork the repository you want to contribute to.
(By forking you create a local copy of the repository under your name.)

2. Once its forked, copy the url either from the methods-

    1. Copy the url from the address bar
    2. Click on the Code drop down button, then copy the url
    3. The url is - https://github.com/<Your_Github_Username>/<Repository_name>.git
    
        For example - If you forked a repository named 'HelloWorld' and your Github username is ASDF
        
        Then the url for the forked repository will be https://github.com/ASDF/HelloWorld.git
     
    4. Open GitBash. Type
    
            git clone "url"
            
          For Example - 
            
            git clone 'https://github.com/ASDF/HelloWorld.git'
          
       (cloning creates a copy of the repository in your computer)
    
    5. Move to the respective folder 
          
              cd RepositoryName
              
          For Example - 
          
              cd HelloWorld
    
        (This takes you to the place where you'll make changes)
        
        or
      
            cd RepositoryName
        
            cd FolderName
      
      (this takes you to the folder in which you want to make changes)
      
     6. Creating a new branch
     
            git checkout -b 'BranchName'
            
          For Example - If your new branch name is 'code'
          
              git checkout -b 'code'
        
        Initially, the branch is master or main (recently changed). So to move to a new branch, we write the above command.
        
     7. Make the changes or add something if you want to.
     
     8. Adding the file
     
            git add 'fileName'
            
          For Example - If you made a chnge in file named Form that contains HTML code:
          
              git add Form.html
            
          or
          
          if there are more than 1 file
          
            git add .
            
     9. To commit the changes - 
     
            git commit -m 'commit message'
            
          For example - 
          
              git commit -m 'Added File'
            
          The commit message should be precise and to the point.
          
     10. Push the changes
     
              git push origin 'BranchName'
              
            Example - 
                
                git push origin code
                
     11. Visit your repository on the browser. Click on 'Compare and Merge'
     
     12. Click 'Create Pull Request'.
     
     13. Congratulations!!!✨ You just submitted your pull request.😅
     
Hope you enjoyed this journey and try to make more and more pull requests and contribute to Open Source!

# **Happy Contibuting**
