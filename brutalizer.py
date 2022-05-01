import sys, getopt
import brute

def main(argv):

    try:
      opts, args = getopt.getopt(argv,'host:port:url:passwords_file:pass_enc_type:username:status_code:')
      try:
        #TODO:This need to be enhanced
        bruteforcer = brute.Brute(args[1],args[3],args[5],args[7],args[9],args[11])
        result = bruteforcer.brutalize()
        print(result)
      except Exception as e:
          print(str(e))
    except getopt.GetoptError as e:
      print (str(e))
      sys.exit(2)
  

if __name__ == "__main__":
   main(sys.argv[1:])