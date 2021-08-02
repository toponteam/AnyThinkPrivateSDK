// Copyright 2004-present Facebook. All Rights Reserved.
//
// You are hereby granted a non-exclusive, worldwide, royalty-free license to use,
// copy, modify, and distribute this software in source code or binary form for use
// in connection with the web services and APIs provided by Facebook.
//
// As with any software that integrates with the Facebook platform, your use of
// this software is subject to the Facebook Developer Principles and Policies
// [http://developers.facebook.com/policy/]. This copyright notice shall be
// included in all copies or substantial portions of the software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
// FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
// COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
// IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
// CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#import <Foundation/Foundation.h>

/**
 * AppLovin Bid Format
 */
typedef NS_ENUM(NSInteger, FBBKAppLovinAdBidFormat) {
    FBBKAppLovinAdBidFormatInterstitial,
    FBBKAppLovinAdBidFormatBanner,
    FBBKAppLovinAdBidFormatMRec,
    FBBKAppLovinAdBidFormatRewardedVideo
};

NS_ASSUME_NONNULL_BEGIN
/**
 * Parameters for AppLovin Bidder
 */
@interface FBBKAppLovinBidderParameters : NSObject
/**
 * Designated Initializer for specific bidder parameters
 * Required for FBBKAppLovinBidder
 * @param appId Application identifer / Main Bundle Identifier
 * @param platformId Platform Identifier for the given bidder
 * @param adBidFormat Advertisment Format parameter for the given bidder
 * @param bidToken Token for bidding. Provided by AppLovin SDK
 */
- (instancetype)initWithAppId:(NSString *)appId
                   platformId:(NSString *)platformId
                  adBidFormat:(FBBKAppLovinAdBidFormat)adBidFormat
                     bidToken:(NSString *)bidToken NS_DESIGNATED_INITIALIZER;
- (instancetype)init NS_UNAVAILABLE;
+ (instancetype)new NS_UNAVAILABLE;
/**
 * Application identifer / Main Bundle Identifier
 * Required parameter and should be passed in the designated initializer
 */
@property (nonatomic, readonly, copy) NSString *appId;
/**
 * Platform Identifier for the given bidder
 * Required parameter and should be passed in the designated initializer
 */
@property (nonatomic, readonly, copy) NSString *platformId;
/**
 * Advertisment Format parameter for the given bidder
 * Required parameter and should be passed in the designated initializer
 */
@property (nonatomic, readonly) FBBKAppLovinAdBidFormat adBidFormat;
/**
 * Token for bidding. Provided by AppLovin SDK
 * Required parameter and should be passed in the designated initializer
 * see https://www.applovin.com/ for more information
 */
@property (nonatomic, readonly, copy) NSString *bidToken;
/**
 * This method sets the Flag indicating if this request is subject to the COPPA regulations
 * established by the USA FTC for the given bidder
 * Default is 'NO'
 */
@property (nonatomic, assign) BOOL coppa;

@end

NS_ASSUME_NONNULL_END
