import re

# Please help complete this tuple
OPERATOR_PREFIX = ['0802', '0803', '0805', '0806', '0807', '0808',
    '0809', '0810', '0813', '0815', '0816', '0819', '0703', '0705']

def is_valid_number(number):
    """
    Consumes a phone number and tries to make sure it is a valid
    Nigerian mobile phone number. It will return True for numbers in the
    following format:

    * 08051119999
    * 0805-111-9999
    * 0805 111 9999
    * 0805.111.9999
    * 0000805-111-9999
    * XXX0805 - 111 - 9999

    #TODO:
    Validate international dialling code also.
    """

    nigerian_number = re.compile(
        """
        # Don't match from the beginning of the string. This makes it
        # inaccurate in truly determining if the number is from Nigeria
        # but smsing will assume that the number is Nigerian
        (\d{4})     #   Match the OPERATOR_PREFIX
        \D*         #   Match any character that isn't a number lazily
        (\d{3})     #   Next 3 digits
        \D*         #   Match any character that isn't a number lazily
        (\d{4})     #   Match last 4 digits
        $           #   End of string
        """
        , re.VERBOSE)
    try:
        broken_number = nigerian_number.search(number).groups()
        try:
            if broken_number[0] in OPERATOR_PREFIX:
                return True
        except IndexError:
                return False
    except AttributeError:
        # If the above re.search().group() fails, it will throw
        # AttributeError
            return False
